# User

## User

Represents the user object.

### Attributes

Name | Type | Description
---- | ---- | -----------
`id` | `snowflake` | The ID of this user
`username` | `str` | The name of the user
`avatar` | `str` | The user's avatar hash
`discriminator` | `str` | The user's discriminator (4-digit discord-tag)
`bot` | `bool` | Whether this user is a bot
`verified` | `bool` | Whether the email on this account has been verified
`email` | `str` | The user's email address

### Properties

#### default\_avatar

Retruns the Default (colored discord logo) avatar URL of the user.

#### avatar\_url

Returns the avatar URL of the user.

#### mention

Returns a formated string that mentions the user.

### Methods

#### get\_avatar\_url(`fmt='webp'`, `size=1024`)

Returns the URL of the user's avatar in a specific format and size.

##### Arguments:
Name | Type | Description
---- | ---- | -----------
`fmt` | `str` | Imageformat of the avatar
`size` | `int` | Size of the avatar

## Presence

Represents the Presence of a user.

### Attributes

Name | Type | Description
---- | ---- | -----------
`user` | [User](USER.md) | 
`game` | [Game](USER.md) | The user's current activity
`status` | `Status`(enum) | The user's current status

## Game

Represents the activity of a user.

### Attributes

Name | Type | Description
---- | ---- | -----------
`type` | `GameType`(enum) | Whether the user is just playing the game or streaming it.
`name` | `str` | Name of the game
`url` | Stream URL. Only validated when `GameType` is `STREAMING`.

## Enums

User specific Enumerations

### Status

 * `ONLINE`
 * `IDLE`
 * `DND` (Do not Disturb)
 * `OFFLINE`

### GameType

 * `DEFAULT` (Playing ...)
 * `STREAMING` (Streaming ...)
