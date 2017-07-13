# The Astrocrash game.
# Based on the classic one Asteroids.

import random, math

# Refactored modules from Livewires package.
import games, color


games.init(screen_width = 640, screen_height = 480, fps = 50)


class Asteroid(games.Sprite):
    """ An asteroid which floats across the screen. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {
        SMALL   :   games.load_image("asteroid_small.bmp"),
        MEDIUM  :   games.load_image("asteroid_med.bmp"),
        LARGE   :   games.load_image("asteroid_big.bmp")
    }
    SPEED = 2
    POINTS = 30
    total = 0

    def __init__(self, x, y, size):
        """ Initialize asteroid sprite. """
        super(Asteroid, self).__init__(image = Asteroid.images[size], x = x, y = y, \
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.radom() / size, \
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.radom() / size)
        self.size = size


class Ship(games.Sprite):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    sound = games.load_sound("thrust.wav")
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        """ Initiazlie ship sprite. """
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0

    def update(self):
        """ Rotate based on keys pressed. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            # change velocity components based on ship's angle
            angle = self.angle * math.pi / 180 # convert to radians

            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # fire missle if spacebar pressed.
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missle = Missle(self.x, self.y, self.angle)
            games.screen.add(new_missle)
            self.missile_wait = Ship.MISSILE_DELAY

        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1


class Missile(games.Sprite):
    """ A missle launched by th player's ship. """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 480
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """ Initialize missile sprite. """
        Missle.sound.play()

        # convert to radians
        angle = ship_angle * math.pi / 180

        # calculate missile's starting position
        buffer_x = Missle.BUFFER * math.sin(angle)
        buffer_y = Missle.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # create the missile
        super(Missile, self).__init__(image = Missile.image, x = x, y = y, dx = dx, dy = dy)

        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Move the missile. """
        # if the lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Game():
    """ A main class to initiate the game and combain everything. """
    def __init__(self):
        """ Initialize Game object. """
        self.level = 0
        self.sound = games.load_sound("level.wav")

        # create a score
        self.score = games = Text(value = 0, size = 30, \
            color = color.white, top = 5, right = games.screen.width - 10, \
            is_collideable = False)
        games.screen.add(self.score)

        # create a player's ship
        self.ship = Ship(game = self, x = games.screen.width / 2, y = games.screen.height /2)
        games.screen.add(self.ship)

    def play(self):
        # begin theme music
        games.music.load("theme.mid")
        games.music.play(-1)

        # load and set background
        bg_image = games.load_image("nebula.jpg")
        games.screen.background = bg_image

        # advance to the next level
        self.advance()

        # start the game
        games.screen.mainloop()

    def advance(self):
        """ Advance to the next game level. """
        self.level += 1

        # amount of space around the ship to preserve when creating asteroids
        BUFFER = 150

        # create new asteroids
        for i in range(self.level):
            # calculate an x an y at least BUFFER distance from the ship
            # choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # choose distance along x-axis and y-axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            # wrap around screen, if necessary
            x %= games.screen.width
            y %= games.screen.height

            # create the asteroid
            new_asteroid = Asteroid(game = self, x = x, y = y, size = Asteroid.LARGE)
            games.screen.add(new_asteroid)

        # display level number
        level_message = games.Message(value = "Level " + str(self.level), size = 40, \
            color = color.yellow, x = games.screen.width / 2, y = games.screen.width / 10, \
            lifetime = 3 * games.screen.fps, is_collideable = False)
        games.screen.add(level_message)

        # play new level sound (except at first level)
        if self.level > 1:
            self.sound.play()

    def end(self):
        """ End the game message. """
        end_message = games.Message(value = "Game Over", size = 90, color = color.red, \
            x = games.screen.width / 2, y = games.screen.height / 2, lifetime = 5 * games.screen.fps, \
            after_death = games.screen.quit, is_collideable = False)
        games.screen.add(end_message)


