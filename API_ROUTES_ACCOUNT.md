# InlineGUI Account API Routes

This document describes the account save/create functionality for InlineGUI.

## Routes

### POST /api/account/register
Creates a new user account.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "user": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### POST /api/account/login
Logs in an existing user.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "token": "jwt-token-here",
  "user": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### GET /api/account/me
Returns the current logged-in user's information.

**Headers:**
```
Authorization: Bearer <token>
```

## Database Integration

For production use, integrate with MongoDB or LevelUP:

### MongoDB Example
```javascript
var mongoose = require('mongoose');
var userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  password: String, // hashed with bcrypt
  createdAt: { type: Date, default: Date.now }
});
var User = mongoose.model('User', userSchema);
```

### LevelUP Example
```javascript
var levelup = require('levelup');
var db = levelup('./inlinegui-users');

db.put('user:john@example.com', JSON.stringify({
  name: 'John Doe',
  email: 'john@example.com',
  createdAt: Date.now()
}), function(err) {
  if (err) console.error('Error saving user:', err);
});
```

## Security Notes

- Always hash passwords with bcrypt before storing
- Use HTTPS for all authentication routes
- Implement rate limiting on login/register endpoints
- Validate and sanitize all user input
- Set secure HTTP-only cookies for session tokens
