var gulp = require('gulp'),     
  sass = require('gulp-ruby-sass') 

var config = {
  sassPath: './assets/styles',
}

gulp.task('sass', function() { 
  return gulp.src('./assets/**/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('./assets/')); 
});

gulp.task('watch', function() {
  gulp.watch(config.sassPath + '/**/*.scss', ['css']); 
});

gulp.task('default', ['sass'], function(){
  var process = require('child_process');
  var spawn = process.spawn;
  var PIPE = {stdio: 'inherit'};
  spawn('python', ['app.py'], PIPE);
});
