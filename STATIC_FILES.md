# Static Files Management

This project uses **npm** to manage vendor dependencies (Bootstrap, jQuery) for easy version pinning and updates.

## Package Versions

### Home Page (Bootstrap 3 theme)
- **Bootstrap**: 3.3.7 (via npm package `bootstrap`)
- **jQuery**: 2.1.4 (via npm package `jquery`)

### Projects Page (Bootstrap 4 theme)
- **Bootstrap**: 4.5.2 (via npm package `bootstrap-4`)
- **jQuery**: 3.5.1 (via npm package `jquery-3`)
- **Popper.js**: 1.16.1 (required for Bootstrap 4)

### Custom/Site-Specific Libraries (kept in static/home/js/)
These remain as local files since they're project-specific:
- `theia-sticky-sidebar.js` - Sticky sidebar functionality
- `isInViewport.js` - Viewport detection
- `stickyfill.min.js` - Polyfill for position: sticky
- `scripts.js` - Custom site scripts

## Updating Dependencies

### To update to a new version:

1. Edit `package.json` to change version numbers
2. Run `npm install`
3. Rebuild Docker container: `docker-compose build`
4. Deploy: `docker-compose up -d`

### Example - Update jQuery:
```json
{
  "dependencies": {
    "jquery": "2.1.5"  // Change from 2.1.4
  }
}
```

## File Locations

### Development
- **npm packages**: `/home/karlok/portfolio-site/node_modules/`
- **Custom files**: `home/static/home/js/`, `home/static/home/css/`

### Production (inside Docker container)
- **All static files collected to**: `/app/staticfiles/`
- **Served via WhiteNoise at**: `http://yoursite.com/static/`

## Deleted Files (Now managed by npm)

The following vendor files were removed from version control:
- ~~`home/static/home/css/bootstrap.css`~~ → Now: `bootstrap/dist/css/bootstrap.min.css`
- ~~`home/static/home/js/jquery-2.1.4.min.js`~~ → Now: `jquery/dist/jquery.min.js`
- ~~`home/static/home/js/bootstrap.min.js`~~ → Now: `bootstrap/dist/js/bootstrap.min.js`
- ~~`projects/static/projects/css/bootstrap-4.5.2.css`~~ → Now: `bootstrap-4/dist/css/bootstrap.min.css`
- ~~`projects/static/projects/js/jquery-3.5.1.js`~~ → Now: `jquery-3/dist/jquery.min.js`
- ~~`projects/static/projects/js/bootstrap-4.5.2.js`~~ → Now: `bootstrap-4/dist/js/bootstrap.bundle.min.js`
- ~~`projects/static/projects/js/popper-1.16.1.js`~~ → Included in `bootstrap.bundle.min.js`

## Benefits

✅ **Version Control**: Pin exact versions in `package.json`
✅ **Easy Updates**: Change version number and run `npm install`
✅ **Smaller Repo**: No vendor files in git (node_modules/ is gitignored)
✅ **Source Maps**: npm packages include source maps for debugging
✅ **Consistency**: Same versions in development and production
