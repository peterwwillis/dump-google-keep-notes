# dump-google-keep-notes

Python script to login to Google Keep, download all your notes, and save them to individual files. Media is not downloaded.

## Usage

1. Configure your ~/.netrc file with your Username and App Password for machine `google.com`.
2. Run `make` in this directory.

If login is successful:
 - A file `google_keep_state.json` will be created in the current directory.
 - A new directory `notes/` will be created.
 - All your notes will be created as files with the filename of the Google Keep ID. The contents will be YAML front-matter of the attributes, and the text body from the note. Since the filename is the Google Keep ID, re-running these scripts should just give you the latest copy of the note.

For some reason the *extracted_text* fields are not coming out, so you may want to dig through the `google_keep_state.json` for those sections if you need them.
