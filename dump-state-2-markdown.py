#!/usr/bin/env python
import gkeepapi
import sys
import os
import json

keep = gkeepapi.Keep()

fh = open('google_keep_state.json', 'r')
state = json.load(fh)
keep.restore(state)
fh.close()

if not os.path.exists("notes"):
    os.mkdir("notes")

gnotes = keep.all()
for note in gnotes:
    fh = open("notes/%s" % note.id, 'w')
    fh.write("---\n")
    fh.write("id: %s\n" % note.id)
    fh.write("title: %s\n" % note.title)
    if note.color != gkeepapi.node.ColorValue.White: 
        fh.write("color: %s\n" % note.color)
    fh.write("archived: %s\n" % note.archived)
    fh.write("pinned: %s\n" % note.pinned)
    if note.labels.all(): 
        fh.write("labels: %s\n" % [x.name for x in note.labels.all()] )

    category, links = [], []
    for annotation in note.annotations.all():
        if type(annotation) is gkeepapi.node.Category:
            category.append(annotation.category)
        if type(annotation) is gkeepapi.node.WebLink:
            links.append({"title": annotation.title, "url": annotation.url, "image_url": annotation.image_url, "description": annotation.description})
    if category: fh.write("category: %s\n" % category)
    if links:    fh.write("links: %s\n" % links)

    fh.write("created_at: %s\n" % note.timestamps.created)
    if note.timestamps.deleted != None and note.timestamps.deleted != note.timestamps.int_to_dt(0):
        fh.write("deleted_at: %s\n" % note.timestamps.deleted)
    if note.timestamps.trashed != note.timestamps.int_to_dt(0): 
        fh.write("trashed_at: %s\n" % note.timestamps.trashed)
    fh.write("edited_at: %s\n" % note.timestamps.edited)
    fh.write("updated_at: %s\n" % note.timestamps.updated)
    if note.collaborators.all() != []: 
        fh.write("collaborators: %s\n" % note.collaborators.all())
    fh.write("---\n")
    fh.write(note.text)
    fh.write("\n")
    fh.close()
