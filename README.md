# Rohan Verma — Portfolio Site

A single-page portfolio site with a Python-developer theme, served through a
tiny Flask app so it can run as a **web service on Render**. The domain
itself (bought on Hostinger) is pointed at Render via DNS — Hostinger isn't
hosting the files, just the domain name.

## Project structure

Put the site in a `static/` folder next to `app.py`, like this:

```
your-repo/
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
└── static/
    └── index.html   <-- your portfolio page goes here
```

If your `index.html` currently sits at the repo root, create a `static`
folder and move it in:

```bash
mkdir static
mv index.html static/index.html
```

## 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial portfolio site"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 2. Deploy on Render

1. Go to [render.com](https://render.com) and sign in with GitHub.
2. Click **New +** → **Web Service**.
3. Select your GitHub repo. Render will detect `render.yaml` automatically
   and pre-fill the build/start commands — otherwise set them manually:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Click **Create Web Service**. Render will build and deploy; you'll get a
   URL like `https://rohan-portfolio.onrender.com`.
5. Any future push to `main` auto-deploys (`autoDeploy: true` in
   `render.yaml`).

## 3. Point your Hostinger domain at Render

In Render, open your service → **Settings** → **Custom Domains** → **Add
Custom Domain**, and enter your domain (e.g. `rohanverma.dev`). Render will
show you the DNS records to add.

Then in **Hostinger** → **Domains** → your domain → **DNS / Name Servers**
→ **DNS Zone Editor**, add the records Render gave you — typically:

| Type  | Name | Value                          |
|-------|------|---------------------------------|
| CNAME | www  | `rohan-portfolio.onrender.com` |
| A     | @    | (the IP Render provides)       |

DNS changes can take anywhere from a few minutes to a few hours to
propagate. Once it does, Render will issue a free SSL certificate for your
domain automatically.

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`.

## Notes

- This is a fully static site technically — Flask here just exists so it
  can run as a **Render web service** instead of Render's separate "Static
  Site" product. If you'd rather use Render's native Static Site hosting
  (no `app.py`/Flask needed at all), that's simpler: just point Render at
  the `static/` folder as the publish directory and skip this Flask layer.
- Update the placeholder name, bio, projects, and experience directly in
  `static/index.html` before deploying.
