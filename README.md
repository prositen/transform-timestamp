# transform-timestamp

This tool reads a CSV where one field contains date-time on one format, and writes a CSV where this field is
replaced with a date-time on another.

* Default input date-time format is unix timestamp (or rather, a string where the first 10 characters are a unix timestamp)
* Default output date-time format is ISO 8601
* Can read from stdin or named file
* Can write to stdout or named file
