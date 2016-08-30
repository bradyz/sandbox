for FILE in $(ls *Song*.java)
do
    USER=$(echo $FILE | sed -e 's/_.*\.java//')
    mkdir tmp
    cp $FILE tmp/Song.java
    cd tmp
    javac Song.java
    DIFF=$(java Song 2> /tmp/Error | diff ../A1_Song_Output.txt -)
    if [[ "$DIFF" != "" ]]
    then
        echo "================================================================="
        echo $USER
        [[ "$(cat /tmp/Error)" != "" ]] && cat /tmp/Error || echo $DIFF
    fi
    cd ..
    rm tmp/*
    rmdir tmp
done
