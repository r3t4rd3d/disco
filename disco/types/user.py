from holster.enum import Enum

from disco.types.base import SlottedModel, Field, snowflake, text, binary, with_equality, with_hash

DefaultAvatars = Enum(
    BLURPLE=0,
    GREY=1,
    GREEN=2,
    ORANGE=3,
    RED=4,
)


class User(SlottedModel, with_equality('id'), with_hash('id')):
    """
    User object.

    Attributes
    ----------
    id : snowflake
        The ID of this user.
    username : str
        The name of the user.
    avatar : str
        The user\'s avatar hash.
    discriminator : str
        The user\'s discriminator (4-digit discord-tag).
    bot : bool
        Whether this user is a bot.
    verified : bool
        Whether the email on this account has been verified.
    email : str
        The user\'s email address.
    """
    id = Field(snowflake)
    username = Field(text)
    avatar = Field(binary)
    discriminator = Field(str)
    bot = Field(bool, default=False)
    verified = Field(bool)
    email = Field(str)

    presence = Field(None)

    def get_avatar_url(self, fmt='webp', size=1024):
        """
        Returns the URL to the user\'s avatar.

        Args
        ----
        fmt : str
            Imageformat of the avatar.
        size : int
            Size of the avatar.

        Returns
        -------
        str
            The URL to the user\'s avatar.
        """
        if not self.avatar:
            return 'https://cdn.discordapp.com/embed/avatars/{}.png'.format(self.default_avatar.value)

        return 'https://cdn.discordapp.com/avatars/{}/{}.{}?size={}'.format(
            self.id,
            self.avatar,
            fmt,
            size
        )

    @property
    def default_avatar(self):
        """
        Returns the Default avatar url of the user.
        """
        return DefaultAvatars[int(self.discriminator) % len(DefaultAvatars.attrs)]

    @property
    def avatar_url(self):
        """
        Returns the avatar url of the user.
        """
        return self.get_avatar_url()

    @property
    def mention(self):
        """
        Formated string that mentions the user.
        """
        return '<@{}>'.format(self.id)

    def open_dm(self):
        return self.client.api.users_me_dms_create(self.id)

    def __str__(self):
        return u'{}#{}'.format(self.username, str(self.discriminator).zfill(4))

    def __repr__(self):
        return u'<User {} ({})>'.format(self.id, self)


GameType = Enum(
    DEFAULT=0,
    STREAMING=1,
)

Status = Enum(
    'ONLINE',
    'IDLE',
    'DND',
    'INVISIBLE',
    'OFFLINE'
)


class Game(SlottedModel):
    """
    Represents the activity of a user.

    Attributes
    ----------
    type : `GameType`
        Whether the user is just playing the game or streaming.

        Possible values are: `DEFAULT` (Playing ...) and `STREAMING` (Streaming ...).
    name : str
        Name of the Game.
    url : str
        Stream URL. Only validated when `GameType` is `STREAMING`.
    """
    type = Field(GameType)
    name = Field(text)
    url = Field(text)


class Presence(SlottedModel):
    """
    Represents the Presence of a user.

    Attributes
    ----------
    user : :class:`disco.types.user.User`
    game : :class:`disco.types.user.Game`
        The user\'s current activity.
    status : `Status`
        The user\'s current status.

        Possible values are: `ONLINE`, `IDLE`, `DND` (Do not Disturb) and `OFFLINE`.
    """
    user = Field(User, alias='user', ignore_dump=['presence'])
    game = Field(Game)
    status = Field(Status)
