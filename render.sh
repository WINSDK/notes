#!/bin/sh

if [ -z $1 ]; then
    echo "Must enter file to render"
    exit
fi

echo '<meta name="viewport" content="width=device-width, initial-scale=1">' > .rendered.html

if [ "$2" = "--color" ] || [ "$2" = "-c" ]; then
    if [ -z $3 ]; then
        echo "Must enter color option"
        exit
    fi

    if [ "$3" = "dark" ]; then
        #echo '<style>body { background-color: #c9d1d9; }</style' > .rendered.html
        echo '<link rel="stylesheet" href="./github-markdown-dark.css">' >> .rendered.html
    elif [ "$3" = "light" ]; then
        echo '<link rel="stylesheet" href="./github-markdown-light.css">' > .rendered.html
    else
        printf "'%s' isn't a valid color option\n" $3
        exit
    fi
else
    echo '<link rel="stylesheet" href="./github-markdown-dark.css">' > .rendered.html
fi

html=$(pandoc --from gfm $1)
read -r -d '' css << EOM
    <style>
        body { background-color: #c9d1d9; }

    	.markdown-body {
    		box-sizing: border-box;
    		min-width: 200px;
    		max-width: 980px;
    		margin: 0 auto;
    		padding: 45px;
    	}
    
    	@media (max-width: 767px) {
    		.markdown-body {
    			padding: 15px;
    		}
    	}
    </style>
EOM

echo "<article class="markdown-body">" >> .rendered.html
echo $css                              >> .rendered.html
echo $html                             >> .rendered.html
echo "</article>"                      >> .rendered.html
chromium-bin .rendered.html > /dev/null 2>&1
