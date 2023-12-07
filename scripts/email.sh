to_email="$EMAIL_VARIABLE"

subject="Pipeline terminou"
body="Pipeline do projeto de C214 terminou"

echo "set smtp-use-starttls" >> ~/.mailrc
echo "set ssl-verify=ignore" >> ~/.mailrc
echo "$body" | mail -s "$subject" "$to_email"