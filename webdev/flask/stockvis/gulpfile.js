var gulp = require('gulp');
var sass = require('gulp-ruby-sass');
var autoprefixer = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var process = require('child_process');

var browserSync = require('browser-sync'),
    reload = browserSync.create().reload;


gulp.task('styles', function() {
  return gulp.src('sass/*.scss')
    .pipe(sass({ style: 'expanded', 'sourcemap=none': true }))
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1'))
    .pipe(gulp.dest('static/css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifycss())
    .pipe(gulp.dest('static/css'));
});

gulp.task('browser-sync', function() {
  browserSync.init(null, {
    proxy: "http://localhost:5001",
    files: ["**/*.*"],
    browser: "google chrome",
    port: 7000,
  });
});

gulp.task('watch', function() {
  gulp.watch('sass/*.scss', ['styles']); 
});

gulp.task('default', ['styles', 'browser-sync', 'watch'], function(){
  process.spawn('python3', ['app.py'], {stdio: 'inherit'});
});
