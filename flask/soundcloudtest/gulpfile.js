var gulp = require('gulp');
var sass = require('gulp-ruby-sass');

gulp.task('sass', function() { 
  return gulp.src('static/css/**/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('static/css')); 
});

gulp.task('watch', function() {
  gulp.watch('static/css/**/*.scss', ['sass']); 
});

gulp.task('default', ['sass', 'watch'], function(){
  var process = require('child_process');
  process.spawn('python', ['app.py'], {stdio: 'inherit'});
});
