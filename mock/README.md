# Add new samples

You can fill the file species.json which will be automatically loaded at the startup of the server.

Or you can POST data to it

{
    http post ip:5000/samples { "speciesName":["sequence", dangerosity], "speciesName2":["sequence", dangerosity]}
}

Dangerosity is a 0 or a 1
