def get_home_page():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Final Project API</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            width: 100%;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { font-size: 3em; color: #333; margin-bottom: 10px; }
        .header .subtitle { color: #666; font-size: 1.2em; }
        .status-badge {
            display: inline-block;
            padding: 8px 20px;
            background: #28a745;
            color: white;
            border-radius: 20px;
            font-size: 0.9em;
            margin-top: 10px;
        }
        .features {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 25px;
            margin: 25px 0;
        }
        .features h3 { color: #333; margin-bottom: 15px; font-size: 1.3em; }
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
        }
        .feature-item { padding: 10px; color: #555; font-size: 1.05em; }
        .feature-item:before { content: "✅ "; }
        .links-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-top: 25px;
        }
        .link-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s ease;
            text-decoration: none;
            color: #333;
            border: 2px solid transparent;
        }
        .link-card:hover {
            background: #667eea;
            color: white;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            border-color: #667eea;
        }
        .link-card .icon { font-size: 2em; display: block; margin-bottom: 8px; }
        .link-card .label { font-weight: 600; font-size: 1.1em; }
        .link-card .description { font-size: 0.85em; opacity: 0.8; margin-top: 5px; display: block; }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #999;
            font-size: 0.9em;
        }
        .footer .tech-stack { margin-top: 8px; }
        .footer .tech-stack span {
            display: inline-block;
            padding: 3px 12px;
            background: #f0f0f0;
            border-radius: 12px;
            margin: 0 5px;
            font-size: 0.85em;
            color: #666;
        }
        @media (max-width: 600px) {
            .container { padding: 20px; }
            .header h1 { font-size: 2em; }
            .links-grid { grid-template-columns: 1fr; }
            .features-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Final Project API</h1>
            <p class="subtitle">CRUD API with JWT Authentication</p>
            <span class="status-badge">● System Online</span>
        </div>
        <div class="features">
            <h3>✨ Features</h3>
            <div class="features-grid">
                <div class="feature-item">User Registration</div>
                <div class="feature-item">JWT Authentication</div>
                <div class="feature-item">CRUD Operations</div>
                <div class="feature-item">Async Database</div>
                <div class="feature-item">Error Handling</div>
                <div class="feature-item">API Documentation</div>
            </div>
        </div>
        <div class="links-grid">
            <a href="/docs" class="link-card">
                <span class="icon">📚</span>
                <span class="label">API Docs</span>
                <span class="description">Swagger UI</span>
            </a>
            <a href="/redoc" class="link-card">
                <span class="icon">📖</span>
                <span class="label">ReDoc</span>
                <span class="description">Alternative Docs</span>
            </a>
            <a href="/users/register" class="link-card">
                <span class="icon">📝</span>
                <span class="label">Register</span>
                <span class="description">Create Account</span>
            </a>
            <a href="/users/login" class="link-card">
                <span class="icon">🔑</span>
                <span class="label">Login</span>
                <span class="description">Get Token</span>
            </a>
        </div>
        <div class="footer">
            <p>Final Project • FastAPI + SQLite + JWT</p>
            <div class="tech-stack">
                <span>FastAPI</span>
                <span>SQLAlchemy</span>
                <span>SQLite</span>
                <span>JWT</span>
            </div>
        </div>
    </div>
</body>
</html>
    """

def get_register_page():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Final Project</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 450px;
            width: 100%;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { font-size: 2em; color: #333; }
        .header p { color: #666; margin-top: 5px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 5px; color: #555; font-weight: 500; }
        .form-group input {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            transition: border-color 0.3s;
        }
        .form-group input:focus { outline: none; border-color: #667eea; }
        .form-group .hint { font-size: 0.85em; color: #999; margin-top: 5px; }
        .btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3); }
        .btn:active { transform: translateY(0); }
        .message {
            margin-top: 20px;
            padding: 12px;
            border-radius: 10px;
            display: none;
        }
        .message.success {
            display: block;
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .message.error {
            display: block;
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .footer { text-align: center; margin-top: 25px; color: #666; }
        .footer a { color: #667eea; text-decoration: none; font-weight: 500; }
        .footer a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📝 Register</h1>
            <p>Create your account</p>
        </div>
        <form id="registerForm">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter username" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Enter email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter password" required minlength="6">
                <div class="hint">Minimum 6 characters</div>
            </div>
            <button type="submit" class="btn">Create Account</button>
        </form>
        <div id="message" class="message"></div>
        <div class="footer">
            Already have an account? <a href="/users/login">Login</a>
        </div>
    </div>
    <script>
        document.getElementById('registerForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const messageDiv = document.getElementById('message');
            try {
                const response = await fetch('/users/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, email, password })
                });
                const data = await response.json();
                if (response.ok) {
                    messageDiv.className = 'message success';
                    messageDiv.textContent = '✅ Registration successful! Redirecting to login...';
                    messageDiv.style.display = 'block';
                    setTimeout(() => { window.location.href = '/users/login'; }, 2000);
                } else {
                    messageDiv.className = 'message error';
                    messageDiv.textContent = '❌ ' + (data.detail || 'Registration failed');
                    messageDiv.style.display = 'block';
                }
            } catch (error) {
                messageDiv.className = 'message error';
                messageDiv.textContent = '❌ Network error. Please try again.';
                messageDiv.style.display = 'block';
            }
        });
    </script>
</body>
</html>
    """

def get_login_page():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Final Project</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 450px;
            width: 100%;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { font-size: 2em; color: #333; }
        .header p { color: #666; margin-top: 5px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 5px; color: #555; font-weight: 500; }
        .form-group input {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            transition: border-color 0.3s;
        }
        .form-group input:focus { outline: none; border-color: #667eea; }
        .btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3); }
        .btn:active { transform: translateY(0); }
        .message {
            margin-top: 20px;
            padding: 12px;
            border-radius: 10px;
            display: none;
        }
        .message.success {
            display: block;
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .message.error {
            display: block;
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .token-display {
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            display: none;
        }
        .token-display.show { display: block; }
        .token-display code {
            display: block;
            padding: 10px;
            background: white;
            border-radius: 5px;
            word-break: break-all;
            font-size: 0.85em;
            margin-top: 10px;
        }
        .footer { text-align: center; margin-top: 25px; color: #666; }
        .footer a { color: #667eea; text-decoration: none; font-weight: 500; }
        .footer a:hover { text-decoration: underline; }
        .flex { display: flex; gap: 10px; margin-top: 10px; }
        .btn-small {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 600;
            transition: transform 0.2s;
        }
        .btn-small:hover { transform: translateY(-2px); }
        .btn-copy { background: #28a745; color: white; }
        .btn-dashboard { background: #17a2b8; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔑 Login</h1>
            <p>Login to your account</p>
        </div>
        <form id="loginForm">
            <div class="form-group">
                <label for="username">Username or Email</label>
                <input type="text" id="username" name="username" placeholder="Enter username or email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter password" required>
            </div>
            <button type="submit" class="btn">Login</button>
        </form>
        <div id="message" class="message"></div>
        <div id="tokenDisplay" class="token-display">
            <strong>✅ Login successful!</strong>
            <p style="margin-top: 5px; font-size: 0.9em; color: #666;">Your access token:</p>
            <code id="tokenValue"></code>
            <div class="flex">
                <button onclick="copyToken()" class="btn-small btn-copy">📋 Copy Token</button>
                <button onclick="goToDashboard()" class="btn-small btn-dashboard">📊 Dashboard</button>
            </div>
        </div>
        <div class="footer">
            Don't have an account? <a href="/users/register">Register</a>
        </div>
    </div>
    <script>
        let currentToken = '';
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const messageDiv = document.getElementById('message');
            const tokenDisplay = document.getElementById('tokenDisplay');
            const formData = new URLSearchParams();
            formData.append('username', username);
            formData.append('password', password);
            try {
                const response = await fetch('/users/token', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: formData
                });
                const data = await response.json();
                if (response.ok) {
                    currentToken = data.access_token;
                    messageDiv.className = 'message success';
                    messageDiv.textContent = '✅ Login successful!';
                    messageDiv.style.display = 'block';
                    document.getElementById('tokenValue').textContent = currentToken;
                    tokenDisplay.className = 'token-display show';
                    localStorage.setItem('access_token', currentToken);
                } else {
                    messageDiv.className = 'message error';
                    messageDiv.textContent = '❌ ' + (data.detail || 'Login failed');
                    messageDiv.style.display = 'block';
                    tokenDisplay.className = 'token-display';
                }
            } catch (error) {
                messageDiv.className = 'message error';
                messageDiv.textContent = '❌ Network error. Please try again.';
                messageDiv.style.display = 'block';
            }
        });
        function copyToken() {
            navigator.clipboard.writeText(currentToken).then(() => {
                alert('Token copied to clipboard!');
            });
        }
        function goToDashboard() {
            window.location.href = '/dashboard';
        }
    </script>
</body>
</html>
    """

def get_dashboard_page():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - Final Project</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f0f2f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        .token-info { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }
        code { display: block; background: white; padding: 10px; border-radius: 5px; word-break: break-all; }
        .btn { 
            display: inline-block; 
            padding: 10px 20px; 
            background: #dc3545; 
            color: white; 
            text-decoration: none; 
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .btn:hover { background: #c82333; }
        .btn-primary { background: #007bff; }
        .btn-primary:hover { background: #0056b3; }
        .btn-success { background: #28a745; }
        .btn-success:hover { background: #218838; }
        .mt-20 { margin-top: 20px; }
        .flex { display: flex; gap: 10px; flex-wrap: wrap; }
        .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }
        .stat-card { background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; }
        .stat-card h3 { color: #333; margin-bottom: 5px; }
        .stat-card p { font-size: 2em; font-weight: bold; color: #667eea; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Dashboard</h1>
        <p>Welcome to your dashboard!</p>
        <div class="stats">
            <div class="stat-card">
                <h3>Items</h3>
                <p id="itemCount">0</p>
            </div>
            <div class="stat-card">
                <h3>Status</h3>
                <p style="color: #28a745; font-size: 1.2em;">✅ Active</p>
            </div>
            <div class="stat-card">
                <h3>User</h3>
                <p id="usernameDisplay" style="font-size: 1.2em;">-</p>
            </div>
        </div>
        <div class="token-info">
            <strong>Your Token:</strong>
            <code id="tokenDisplay">Loading...</code>
        </div>
        <div class="flex">
            <button onclick="logout()" class="btn">Logout</button>
            <a href="/items-page" class="btn btn-primary">📦 Manage Items</a>
            <a href="/" class="btn btn-success">🏠 Home</a>
        </div>
    </div>
    <script>
        const token = localStorage.getItem('access_token');
        if (!token) {
            window.location.href = '/users/login';
        } else {
            document.getElementById('tokenDisplay').textContent = token;
        }
        
        // Получаем информацию о пользователе
        fetch('/users/me', {
            headers: { 'Authorization': `Bearer ${token}` }
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById('usernameDisplay').textContent = data.username;
        })
        .catch(() => {
            document.getElementById('usernameDisplay').textContent = 'Error';
        });
        
        // Получаем количество товаров
        fetch('/items/', {
            headers: { 'Authorization': `Bearer ${token}` }
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById('itemCount').textContent = data.length || 0;
        })
        .catch(() => {
            document.getElementById('itemCount').textContent = '?';
        });
        
        function logout() {
            localStorage.removeItem('access_token');
            window.location.href = '/users/login';
        }
    </script>
</body>
</html>
    """

def get_items_page():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Items - Final Project</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f0f2f5; }
        .container { max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        .item { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .item:hover { background: #f8f9fa; }
        .item h3 { margin: 0; color: #333; }
        .item .price { color: #28a745; font-weight: bold; font-size: 1.2em; }
        .btn { 
            display: inline-block; 
            padding: 8px 16px; 
            background: #007bff; 
            color: white; 
            text-decoration: none; 
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .btn:hover { background: #0056b3; }
        .btn-danger { background: #dc3545; }
        .btn-danger:hover { background: #c82333; }
        .btn-success { background: #28a745; }
        .btn-success:hover { background: #218838; }
        .flex { display: flex; gap: 10px; flex-wrap: wrap; margin: 20px 0; }
        .loading { text-align: center; padding: 40px; color: #666; }
        #itemsList { margin-top: 20px; }
        .empty { text-align: center; padding: 40px; color: #999; }
        .item-meta { color: #999; font-size: 0.85em; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📦 My Items</h1>
        <div class="flex">
            <a href="/" class="btn">🏠 Home</a>
            <a href="/dashboard" class="btn btn-success">📊 Dashboard</a>
            <button onclick="logout()" class="btn btn-danger">Logout</button>
        </div>
        <div id="itemsList" class="loading">Loading...</div>
    </div>
    <script>
        const token = localStorage.getItem('access_token');
        if (!token) {
            window.location.href = '/users/login';
        }
        
        function logout() {
            localStorage.removeItem('access_token');
            window.location.href = '/users/login';
        }
        
        fetch('/items/', {
            headers: { 'Authorization': `Bearer ${token}` }
        })
        .then(res => {
            if (!res.ok) throw new Error('Failed to fetch');
            return res.json();
        })
        .then(data => {
            if (data.length === 0) {
                document.getElementById('itemsList').innerHTML = `
                    <div class="empty">
                        <h3>📭 No items yet</h3>
                        <p>Create your first item using the API!</p>
                        <p style="font-size: 0.9em; color: #999;">
                            POST /items/ with title, description and price
                        </p>
                    </div>
                `;
                return;
            }
            let html = '';
            data.forEach(item => {
                html += `
                    <div class="item">
                        <h3>${item.title}</h3>
                        <p>${item.description || 'No description'}</p>
                        <p class="price">$${item.price.toFixed(2)}</p>
                        <div class="item-meta">
                            Created: ${new Date(item.created_at).toLocaleDateString()}
                            ${item.updated_at ? ' • Updated: ' + new Date(item.updated_at).toLocaleDateString() : ''}
                        </div>
                    </div>
                `;
            });
            document.getElementById('itemsList').innerHTML = html;
        })
        .catch(err => {
            document.getElementById('itemsList').innerHTML = `
                <div class="empty" style="color: red;">
                    <h3>❌ Error</h3>
                    <p>Failed to load items: ${err.message}</p>
                </div>
            `;
        });
    </script>
</body>
</html>
    """