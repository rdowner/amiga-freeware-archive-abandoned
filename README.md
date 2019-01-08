<!--
   Copyright 2019 Richard Downer

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

Amiga Freeware Archive
======================

This repository contains everything needed to deploy an instance of the Amiga Freeware Archive, apart from the freeware archives themselves.

**This is a work in progress. It does not yet contain "everything" needed!**


In this repository
------------------

[Full documentation](docs) in ReStructured Text format and processed using Read The Docs.

[JSON schemas](json-schemas) that specify the data formats used in the archive.

[Web frontend](web) for browsing and searching the archive.

[AWS SAM application](backend-app) for the backend services.

[CloudFormation](cloudformation) for AWS resources not specifically part of the backend app, such as the data storage.

[Import tooling](import-tools) for importing artifacts and metadata into the archive.
