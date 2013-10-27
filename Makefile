
all:css

css:assets/css/main.css

assets/css/main.css : sass/main.scss sass/mixins.scss sass/style.scss
	sass sass/main.scss:assets/css/main.css --cache-location /tmp --style compressed
