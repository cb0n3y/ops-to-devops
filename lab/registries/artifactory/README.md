# Artifactory and Xray

ToDo

## Name
Artifactory and Xray

## Description

Later dudes!

### Section 1: AQL + JFrog CLI 

In this section, we harness the power of AQL (Artifactory Query Language) and JFrog CLI to optimize package management. Central to this integration is the "JSON_FILE" variable, which plays a pivotal role. The value assigned to this variable should correspond to one of the JSON files stored in the "files" folder. These JSON files contain configuration settings and parameters for package management tasks.

Additionally, the execution of these tasks is orchestrated via a GitLab Pipeline Schedule, ensuring automated and efficient package management operations.

### Section 2: Bash Scripts + JFrog CLI

**Script Behavior:**

1. **Initialization:**
   - The script is written in Bash and begins by initializing several variables, including:
     - `API_PATH`: The path to the API for managing packages.
     - `REPO_NAME`: The name of the repository.
     - `REPO_SUBPATH`: The subpath within the repository.
     - `PACKAGES_TO_HOLD`: The number of packages to retain (default is 3).
     - `DELETE_PACKAGES`: A flag to indicate whether to delete packages (default is false).
     - `VIEW_PACKAGES`: A flag to indicate whether to view packages (default is true).

2. **Command Line Options:**
   - The script uses `getopts` to process command-line options. Users can specify the following options:
     - `-R`: Set the repository name.
     - `-s`: Set the repository subpath.
     - `-n`: Set the number of packages to hold.
     - `-d`: Enable package deletion.
     - `-v`: Enable package viewing.

3. **Validation:**
   - The script checks if the `REPO_NAME` is provided as it is a required parameter. If it is missing, an error message is displayed, and the script exits.

4. **Package Retrieval:**
   - The script uses the `jf rt curl` command to retrieve a list of package URIs from the specified repository and subpath. It then processes and stores these package names in an array called `package_names`.

5. **Sorting Packages:**
   - The retrieved package names are sorted by creation date in descending order. The script saves the last `PACKAGES_TO_HOLD` packages in the `n_package_names` array.

6. **Viewing Packages:**
   - The `-v` option is enabled per default. The script displays the names of the last `PACKAGES_TO_HOLD` packages that are being retained.

7. **Deleting Packages:**
   - If the `-d` option is enabled, the script goes through the list of all packages and deletes those that are not in the `n_package_names` array. It displays the deleted packages and provides an option to uncomment a line to actually delete them.

## Support
This GitLab script delivers a comprehensive package management solution, seamlessly integrating with JFrog CLI and GitLab Pipelines. Whether through dynamic Bash operations or precise AQL queries, it empowers you to maintain a well-organized and efficient repository.
If you encounter any issues, have questions, or need assistance with this project, please don't hesitate to reach out. You can find help and support in the following ways:

* E-Mail: Feel free to contact us via email at cb0n3y@gmail.com for direct support.

## Contributing

If you have any suggestions and/or contributions. Please contact me at : cb0n3y@gmail.com

## Authors and acknowledgment
I would like to extend my heartfelt appreciation to all the contributors who have dedicated their time and expertise to this project. Your valuable contributions have been instrumental in its success. Thank you for being an essential part of our team.

**Authors:**
- [cb0n3y](https://github.com/cb0n3y)

**Contributors:**

## License
Apache License 2.0, see [LICENSE](https://github.com/cb0n3y/artifactory_and_xray/blob/main/LICENSE).
