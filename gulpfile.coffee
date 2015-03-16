require('coffee-script/register')

Q = require('q')
cp = require('child_process')
fs = require('fs')

gulp = require('gulp')
g = require('gulp-load-plugins')()
del = require('delete')
mainBowerFiles = require('main-bower-files')

CONFIG = {
  bowerSrc: './frontend/build/bower_components'
  lessCssSrc: './frontend/lesscss'
  gulpDest: './backend/kegstarter/static/build'
  externalJs: 'vendor.js'
  externalJsMin: 'vendor.min.js'
  allCoffee: [
    './frontend/**/*.coffee'
    'gulpfile.coffee'
  ]
}

gulp.task('default', ['lint', 'django-staticfiles'], ->
  g.util.log('default task finished')
)

gulp.task('watch', ['watchLess'])

gulp.task('watchLess', ->
  gulp.watch([
    CONFIG.lessCssSrc + '/**/*.less'
  ], ['less'])
)

gulp.task('clean', ->
  del(CONFIG.gulpDest,(err) -> if err then g.util.log(err))
)


# Install all the bower requirements (e.g. jQuery, bootstrap etc.)
gulp.task('bower', ->
  g.bower()
)

# After installing all the bower components, concat all the main files from
# them together
gulp.task('minifyBower', ['bower'], ->
  filter = g.filter('**/*.js')
  # If there's a .min file next to this file, remove this file from the list.
  # the gulp.src will catch min files on it's own
  # TODO: It'd be /really/ sweet to replace it in place
  filesToMinify = []
  jsMinFilter = (val, idx, arr) ->
    name = val.split('.')
    name = name.slice(0, -1).join('.') + '.min.' + name[name.length - 1]
    if fs.existsSync(name)
      filesToMinify.push(name)
    else
      filesToMinify.push(val)
    return true
  # Call mainBowerFiles just to populate filesToMinify, because arrays...
  # Using mainBowerFiles also allows us to define 'overrides' in bower.json and
  # get rid of package dependencies as well as control what files are included
  # (aka get bootstrap without the js file and jQuery)
  mainBowerFiles({includeDev: true, filter: jsMinFilter})

  gulp.src(filesToMinify)
    #{base: CONFIG.bowerSrc})
    .pipe(filter)
    .pipe(g.sourcemaps.init({loadMaps: true}))
    .pipe(g.concat(CONFIG.externalJs))
    .pipe(g.uglify(CONFIG.externalJs, {mangle: false, compress: false}))
    .pipe(g.sourcemaps.write('./'))
    .pipe(gulp.dest(CONFIG.gulpDest))
)

# Compile our custom less
gulp.task('less', ['bower'], ->
  gulp.src(CONFIG.lessCssSrc + '/kegstarter.bootstrap.less')
    .pipe(g.sourcemaps.init())
    .pipe(g.less())
    .pipe(g.sourcemaps.write('./'))
    .pipe(gulp.dest(CONFIG.gulpDest + '/css'))
)

# Copy fonts from bootstrap into the static folder
# TODO: This should only copy them on change...
gulp.task('linkFonts', ['bower'], ->
  gulp.src(CONFIG.bowerSrc + '/bootstrap/fonts/*.*')
    .pipe(g.symlink(CONFIG.gulpDest + '/fonts/'))
)

gulp.task('django-staticfiles', ['less', 'linkFonts', 'minifyBower'], ->
  # Return a promise later so we can signal the gulp streaming system cleanly
  config = if process.env.DJANGO_CONFIGURATION then process.env.DJANGO_CONFIGURATION else "Local"
  deferred = Q.defer()
  cp.exec(
    'manage.py collectstatic --noinput --settings kegstarter.config.settings ' +
    '--configuration ' + config,
    (err, stdout, stderr) ->
      g.util.log(stdout)
      if(stderr)
        g.util.log(g.util.colors.red(stderr))
      if(err)
        g.util.log(g.util.colors.red(err))
      deferred.resolve()
  )
  return deferred.promise
)

gulp.task 'lint', ->
  gulp.src(CONFIG.allCoffee)
    .pipe(g.coffeelint())
    .pipe(g.coffeelint.reporter())


gulp.task 'test', ['lint'], ->
  undefined
