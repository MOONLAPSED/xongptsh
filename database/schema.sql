/* SQL DB API SPEC FOR LLM cntnt and cntnt_dtb (content and content database) by printzn@github MIT license
=================================================================================
Entity - A data model that defines the system, with relationships to other entities. An entity is not an instance of an object, but rather a definition or blueprint.

Attribute - A specific data point that an entity defines itself as having. Examples include the "dog" entity, which has attributes such as having four legs and being carnivorous, as well as unique attributes for individual iterations.

Iteration - An instance of an entity created based on the entity's definition and attributes, representing a specific object, event, or concept in the real world that can be represented with the available data types. Iterations can be categorized and modeled by entities.

Data Types - The available data types are:

- TEXT - a string of text
- INTEGER - a whole number
- REAL - a decimal number
- BLOB - a binary large object or a file that is too big to fit in a single column
- VARCHAR(255) - a restricted-length char

Nucleus Tables - The nucleus tables for the vanilla SQLite3 db are:

- text_entries - A table containing information about text entries, including the text entry name, file name, file path, file type, and text entry ID (primary key).
- embeddings - A table containing information about embeddings, including the embedding ID, model ID, and vector (primary key).
- models - A table containing information about models, including the model ID, model name, and model description.
- unix_filesystem - A table containing information about the Unix filesystem, including the inode, PID, systemd_host_file, etc.
=================================================================================
*/

/*
-- TABLES_REF:
    -- bitwise_and // BLOB bitwise math operation
    -- bitwise_cat // catenate two binary blobs
    -- bitwise_not // NOT a binary blob
    -- bitwise_or // OR two binary blobs
    -- bitwise_xor // XOR two binary blobs
    -- bool_string
    -- bool_when
    -- bytes_when  
    -- cli_payloads
    -- credentials
    -- embeddings
    -- entity_embedding
    -- entity_key
    -- entities //the atomic unit of the db - will, after abstraction, always be a unix file system object
    -- exe_when
    -- models
    -- nfs_mounts
    -- ssh_sessions
    -- printf_when
    -- process_status
    -- tcp_sessions
    -- text_entries
    -- text_tags
    -- thread_process_status
    -- unix_filesystem
    -- utime_value
    -- utimes
    -- data
    -- key_vectors
    -- value_vectors
    -- processed_data
*/