
all: css

css : sass/main.scss
	sass sass/main.scss:assets/css/main.css --style compressed
