# The Astrocrash game.
# Based on the classic one Asteroids.


"""
### TO-DO:
    Improve the Astrocrash game by creating a new kind of deadly
    space debris. Give this new type of debris some quality that
    differentiates it from the asteroids. For example, maybe the
    debris requires two missile strikes to be destroyed.
###
"""


import random, math

# Refactored modules from Livewires package.
import games, color


games.init(screen_width = 640, screen_height = 480, fps = 50)


class Wrapper(games.Sprite):
    """ A sprite that wraps around the screen. """
    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Destroy self. """
        self.destroy()


class Collider(Wrapper):
    """ A Wrapper that could collide with another object. """
    def update(self):
        """ Check for overlapping sprites """
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy self and leave explosion behind. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Asteroid(Wrapper):
    """ An asteroid which floats across the screen. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPEED = 2
    SPAWN = 2
    POINTS = 30

    total = 0
    images = {
        SMALL   :   games.load_image("asteroid_small.bmp"),
        MEDIUM  :   games.load_image("asteroid_med.bmp"),
        LARGE   :   games.load_image("asteroid_big.bmp")
    }

    def __init__(self, game, x, y, size):
        """ Initialize asteroid sprite. """
        super(Asteroid, self).__init__(image = Asteroid.images[size], x = x, y = y, \
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size, \
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size
        self.game = game
        Asteroid.total += 1

    def die(self):
        """ Destroy asteroid. """
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        # if asteroid isn't small, replace with two smaller asteroids
        if self.size != Asteroid.SMALL:
            for _ in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game, x = self.x, y = self.y, size = self.size - 1)
                games.screen.add(new_asteroid)

        # if all asteroids are gone, advance to next level.
        if Asteroid.total == 0:
            self.game.advance()

        super(Asteroid, self).die()


class Ship(Collider):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")
    ROTATION_STEP = 3
    VELOCITY_STEP = .04
    MISSILE_DELAY = 20
    VELOCITY_MAX = 5

    def __init__(self, game, x, y):
        """ Initiazlie ship sprite. """
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        """ Rotate based on keys pressed. """
        super(Ship, self).update()

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

            # cap velocity in each direction
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        # fire missle if spacebar pressed and missle wait is over.
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1

    def die(self):
        """ Destroy ship and end the game. """
        self.game.end()
        super(Ship, self).die()


class Missile(Collider):
    """ A missle launched by th player's ship. """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 8
    LIFETIME = 50

    def __init__(self, ship_x, ship_y, ship_angle):
        """ Initialize missile sprite. """
        Missile.sound.play()

        # convert to radians
        angle = ship_angle * math.pi / 180

        # calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
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
        super(Missile, self).update()

        # if the lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    """ Explosion animation. """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp", "explosion2.bmp", "explosion3.bmp", "explosion4.bmp", \
        "explosion5.bmp", "explosion6.bmp", "explosion7.bmp", "explosion8.bmp", "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images, x = x, y = y, \
            repeat_interval = 4, n_repeats = 1, is_collideable = False)
        Explosion.sound.play()


class Game():
    """ A main class to initiate the game and combain everything. """
    def __init__(self):
        """ Initialize Game object. """
        self.level = 0
        self.sound = games.load_sound("level.wav")

        # create a score
        self.score = games.Text(value = 0, size = 30, \
            color = color.white, top = 5, right = games.screen.width - 10, \
            is_collideable = False)
        games.screen.add(self.score)

        # create a player's ship
        self.ship = Ship(game = self, x = games.screen.width / 2, y = games.screen.height / 2)
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
        for _ in range(self.level):
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


def main():
    astrocrash = Game()
    astrocrash.play()

# kick it off!
main()