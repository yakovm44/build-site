from flask import Flask, render_template_string

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dummy Site</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f0f2f5; color: #333; }
        header {
            background: #4a90e2;
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header h1 { font-size: 1.8rem; }
        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
            font-size: 1rem;
        }
        nav a:hover { text-decoration: underline; }
        .hero {
            background: linear-gradient(135deg, #4a90e2, #7b2ff7);
            color: white;
            text-align: center;
            padding: 80px 20px;
        }
        .hero h2 { font-size: 2.5rem; margin-bottom: 15px; }
        .hero p { font-size: 1.2rem; margin-bottom: 30px; }
        .hero a {
            background: white;
            color: #4a90e2;
            padding: 12px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
        }
        .cards {
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 50px 20px;
            flex-wrap: wrap;
        }
        .card {
            background: white;
            border-radius: 10px;
            padding: 30px;
            width: 250px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .card .icon { font-size: 2.5rem; margin-bottom: 15px; }
        .card h3 { margin-bottom: 10px; color: #4a90e2; }
        footer {
            background: #333;
            color: #aaa;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <header>
        <h1>🌐 DummySite</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <div class="hero">
        <h2>Welcome to Dummy Site</h2>
        <p>A simple placeholder website built with Python & Flask.</p>
        <a href="/about">Learn More</a>
    </div>

    <div class="cards">
        <div class="card">
            <div class="icon">🚀</div>
            <h3>Fast</h3>
            <p>Lightweight and quick to load on any device.</p>
        </div>
        <div class="card">
            <div class="icon">🎨</div>
            <h3>Stylish</h3>
            <p>Clean design with modern CSS styling.</p>
        </div>
        <div class="card">
            <div class="icon">🐍</div>
            <h3>Python</h3>
            <p>Powered by Flask, a micro web framework.</p>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 DummySite. Built with Python &amp; Flask.</p>
    </footer>
</body>
</html>
"""

ABOUT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About - Dummy Site</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; color: #333; }
        header { background: #4a90e2; color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        header h1 { font-size: 1.8rem; }
        nav a { color: white; text-decoration: none; margin-left: 20px; }
        nav a:hover { text-decoration: underline; }
        .content { max-width: 700px; margin: 60px auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h2 { color: #4a90e2; margin-bottom: 15px; }
        p { line-height: 1.7; margin-bottom: 15px; }
        footer { background: #333; color: #aaa; text-align: center; padding: 20px; margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <h1>🌐 DummySite</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <div class="content">
        <h2>About This Site</h2>
        <p>This is a dummy website created with Python and Flask to demonstrate a simple multi-page web application.</p>
        <p>It includes a home page, an about page, and a contact page — all served from a single Python script.</p>
        <p>Feel free to use this as a starting point for your own projects!</p>
    </div>
    <footer><p>&copy; 2025 DummySite. Built with Python &amp; Flask.</p></footer>
</body>
</html>
"""

CONTACT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact - Dummy Site</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; color: #333; }
        header { background: #4a90e2; color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        header h1 { font-size: 1.8rem; }
        nav a { color: white; text-decoration: none; margin-left: 20px; }
        nav a:hover { text-decoration: underline; }
        .content { max-width: 600px; margin: 60px auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h2 { color: #4a90e2; margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea {
            width: 100%; padding: 10px; margin-bottom: 20px;
            border: 1px solid #ccc; border-radius: 5px; font-size: 1rem;
        }
        button {
            background: #4a90e2; color: white; border: none;
            padding: 12px 30px; border-radius: 25px; font-size: 1rem; cursor: pointer;
        }
        button:hover { background: #357abd; }
        footer { background: #333; color: #aaa; text-align: center; padding: 20px; margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <h1>🌐 DummySite</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <div class="content">
        <h2>Contact Us</h2>
        <form>
            <label for="name">Name</label>
            <input type="text" id="name" placeholder="Your name">
            <label for="email">Email</label>
            <input type="email" id="email" placeholder="your@email.com">
            <label for="message">Message</label>
            <textarea id="message" rows="5" placeholder="Write your message here..."></textarea>
            <button type="submit">Send Message</button>
        </form>
    </div>
    <footer><p>&copy; 2025 DummySite. Built with Python &amp; Flask.</p></footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME_HTML)


@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML)


@app.route("/contact")
def contact():
    return render_template_string(CONTACT_HTML)


if __name__ == "__main__":
    print("Starting Dummy Site at http://localhost:5000")
    app.run(debug=True, port=5000)