URLs and Routes
===============

Home page
---------

/


Library details
---------------

/library/{library_id}

Examples:
- /library/fish
- /library/17bit


Volume details (where library does not have collections)
--------------------------------------------------------

/library/{library_id}/volume/{volume_id}

Examples:

- /library/fish/volume/352
- /library/17bit/volume/1289


Volume details (where library has collections)
----------------------------------------------

/library/{library_id}/collection/{collection_id}/volume/{volume_id}

Examples:

- /library/software2000/collection/games/volume/101
- /library/software2000/collection/demos/volume/89


Artifact details (where library is not organised by volume)
-----------------------------------------------------------

/library/{library_id}/collection/{collection_id}/artifact/{artifact_id}

Examples:

- /library/aminet/collection/util-net/artifact/foo.lha
- /library/aminet/collection/demo-4k/artifact/bar.lzx
