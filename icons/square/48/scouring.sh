while read p; do
  scour -i "$p" -o "0_$p" --disable-style-to-xml --renderer-workaround --strip-xml-prolog --remove-titles --remove-descriptions --remove-metadata --remove-descriptive-elements --enable-comment-stripping
done
