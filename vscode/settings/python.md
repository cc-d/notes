# Python Development Options in Visual Studio Code

When working with Python in Visual Studio Code, you can customize various settings to enhance your development experience. Here is a comprehensive list of options you can configure in your `settings.json` file:
## Autopep8

- `python.formatting.autopep8Args`: Additional arguments to pass to autopep8.
- `python.formatting.autopep8Path`: Specifies the path to the autopep8 executable.

## Autocomplete

- `python.autoComplete.addBrackets`: Specifies whether Brackets should be added after function and class completions.
- `python.autoComplete.extraPaths`: Specifies additional paths for the autocomplete engine to search through.
- `python.autoComplete.preloadModules`: Specifies modules that should be preloaded to speed up intellisense.
- `python.autoComplete.showAdvancedMembers`: Determines whether advanced members of objects (i.e., members starting with _) are included in autocomplete.

## Analysis

- `python.analysis.autoImportCompletions`: Automatically imports missing symbols in completions.
- `python.analysis.autoSearchPaths`: Automatically searches for import paths.
- `python.analysis.diagnosticSeverityOverrides`: Overrides diagnostic severities.
- `python.analysis.extraPaths`: Additional paths to be used for type checking and analysis.
- `python.analysis.typeshedPaths`: Additional paths to search for typeshed stubs.
- `python.analysis.useLibraryCodeForTypes`: Use library implementations to extract type information when type stubs are not available.

## Bandit

- `python.linting.banditArgs`: Additional arguments to pass to Bandit.
- `python.linting.banditEnabled`: Specifies whether Bandit linting is enabled.
- `python.linting.banditPath`: Specifies the path to the Bandit executable.

## Black

- `python.formatting.blackArgs`: Additional arguments to pass to Black.
- `python.formatting.blackPath`: Specifies the path to the Black executable.

## Debugging

- `python.debug.openDebug`: Controls the behavior of the "Debug Current Test" CodeLens.
- `python.debug.promptToConfigure`: Specifies whether to prompt to configure a debug configuration if potential debug configurations are found.
- `python.debug.configurations`: Configuration options for the Python debugger.
- `python.debug.autoAttach`: Automatically attaches the debugger.

## Environment

- `python.envFile`: Specifies the path to the environment file.
- `python.experiments.enabled`: Specifies whether experimental features should be enabled.
- `python.experiments.optInto`: Specifies which experimental features to opt into.
- `python.experiments.optOutFrom`: Specifies which experimental features to opt out from.

## Formatting

- `python.formatting.formatOnSaveTimeout`: Specifies the timeout for format on save.
- `python.formatting.provider`: Specifies the provider for formatting (`autopep8`, `black`, `yapf`).

## Flake8

- `python.linting.flake8Args`: Additional arguments to pass to Flake8.
- `python.linting.flake8Enabled`: Specifies whether Flake8 linting is enabled.
- `python.linting.flake8Path`: Specifies the path to the Flake8 executable.

## General Python Settings

- `python.pythonPath`: Specifies the path to Python installation.
- `python.autoUpdateLanguageServer`: Automatically update the Python Language Server.
- `python.showStartPage`: Show the Python start page on startup.

## Jedi

- `python.jediEnabled`: Specifies whether Jedi is enabled.
- `python.jediMemoryLimit`: Maximum size of the Jedi HTTP cache.
- `python.jediPath`: Specifies the path to the Jedi executable.

## Linting

- `python.linting.enabled`: Specifies whether linting is enabled.
- `python.linting.ignorePatterns`: Patterns for files and folders to be ignored by the linter.
- `python.linting.lintOnSave`: Specifies whether linting should run on file save.
- `python.linting.maxNumberOfProblems`: Maximum number of linting problems reported per file.
- `python.linting.pycodestyleArgs`: Additional arguments to pass to pycodestyle.
- `python.linting.pycodestyleEnabled`: Specifies whether pycodestyle linting is enabled.
- `python.linting.pycodestylePath`: Specifies the path to the pycodestyle executable.
- `python.linting.pydocstyleArgs`: Additional arguments to pass to Pydocstyle.
- `python.linting.pydocstyleEnabled`: Specifies whether Pydocstyle linting is enabled.
- `python.linting.pydocstylePath`: Specifies the path to the Pydocstyle executable.
- `python.linting.pylintArgs`: Additional arguments to pass to Pylint.
- `python.linting.pylintEnabled`: Specifies whether Pylint linting is enabled.
- `python.linting.pylintPath`: Specifies the path to the Pylint executable.
- `python.linting.pylintUseMinimalCheckers`: Specifies whether Pylint uses minimal checkers.

## Mypy

- `python.linting.mypyArgs`: Additional arguments to pass to Mypy.
- `python.linting.mypyEnabled`: Specifies whether Mypy linting is enabled.
- `python.linting.mypyPath`: Specifies the path to the Mypy executable.

## Notebook

- `python.dataScience.allowImportFromNotebook`: Specifies whether importing of Jupyter notebooks is allowed.
- `python.dataScience.enabled`: Specifies whether the data science features are enabled.
- `python.dataScience.sendSelectionToInteractiveWindow`: Specifies whether the selected code in the file is sent to the interactive window.

## Poetry

- `python.poetryPath`: Specifies the path to the Poetry executable.

## Prospector

- `python.linting.prospectorArgs`: Additional arguments to pass to Prospector.
- `python.linting.prospectorEnabled`: Specifies whether Prospector linting is enabled.
- `python.linting.prospectorPath`: Specifies the path to the Prospector executable.

## Python Environment

- `python.autoComplete.extraPaths`: Additional paths for autocompletion.
- `python.autoUpdateLanguageServer`: Specifies whether the Python Language Server is updated automatically.
- `python.disableInstallationCheck`: Disables the check whether Python is installed.
- `python.experiments.enabled`: Specifies whether experiments are enabled.
- `python.experiments.optInto`: Lists experiments to opt into.
- `python.experiments.optOutFrom`: Lists experiments to opt out from.
- `python.formatting.autopep8Args`: Additional arguments to pass to autopep8.
- `python.formatting.autopep8Path`: Specifies the path to the autopep8 executable.
- `python.formatting.blackArgs`: Additional arguments to pass to Black.
- `python.formatting.blackPath`: Specifies the path to the Black executable.
- `python.formatting.provider`: Specifies the provider for formatting (autopep8, black, yapf).
- `python.formatting.yapfArgs`: Additional arguments to pass to YAPF.
- `python.formatting.yapfPath`: Specifies the path to the YAPF executable.
- `python.globalModuleInstallation`: Specifies whether modules are installed globally.

## Pyright

- `python.analysis.diagnosticMode`: The level of diagnostics produced by Pyright.
- `python.analysis.typeCheckingMode`: Specifies the level of type checking performed.
- `python.analysis.autoSearchPaths`: Specifies whether extra paths are automatically added to search paths.
- `python.analysis.extraPaths`: Specifies extra paths for analysis.

## Testing

- `python.testing.autoTestDiscoverOnSaveEnabled`: Specifies whether test discovery is run on file save.
- `python.testing.pytestPath`: Specifies the path to the pytest executable.
- `python.testing.unittestEnabled`: Specifies whether unittest is enabled.

## Miscellaneous

- `python.pythonPath`: Specifies the path to the Python interpreter.
- `python.sortImports.path`: Specifies the path to the isort module.
- `python.terminal.activateEnvironment`: Specifies whether the Python environment is activated in the terminal.

## Workspace

- `python.workspaceSymbols.building`: Specifies the message to display while building workspace symbols.
- `python.workspaceSymbols.enabled`: Specifies whether workspace symbols are enabled.
- `python.workspaceSymbols.excludes`: Specifies files and folders to exclude from workspace symbol search.
- `python.workspaceSymbols.rebuildOnFileSave`: Specifies whether to rebuild workspace symbols on file save.
- `python.workspaceSymbols.rebuildOnStart`: Specifies whether to rebuild workspace symbols when a workspace is opened.
- `python.workspaceSymbols.tagFilePath`: Specifies the path to the tag file for workspace symbols.

## Language Server

- `python.languageServer`: Specifies the language server to be used for Python.
- `python.autoComplete.addBrackets`: Specifies whether to add brackets when completing function calls.
- `python.autoComplete.showAdvancedMembers`: Specifies whether to show advanced members in IntelliSense.
- `python.autoComplete.preselectInterpreters`: Specifies whether to preselect interpreters in IntelliSense.
- `python.analysis.memory.keepLibraryAst`: Specifies whether to keep libraries' ASTs in memory.
- `python.analysis.memory.keepLibraryLocalVariables`: Specifies whether to keep libraries' local variables in memory.
- `python.analysis.memory.maxMemory`: Specifies the maximum memory size for the analysis process.
- `python.analysis.memory.percentMemory`: Specifies the percent of total memory for the analysis process.

## Jupyter

- `python.dataScience.enabled`: Specifies whether the Jupyter notebook support is enabled.
- `python.dataScience.jupyterServerURI`: Specifies the URI for the Jupyter server.
- `python.dataScience.notebookFileRoot`: Specifies the root directory for notebooks.
- `python.dataScience.sendSelectionToInteractiveWindow`: Specifies whether the selected code is sent to the interactive window.
- `python.dataScience.showCellInputCodeLens`: Specifies whether the code lens is shown for cell input.
- `python.dataScience.showCellOutputCodeLens`: Specifies whether the code lens is shown for cell output.
- `python.dataScience.showJupyterVariableExplorer`: Specifies whether the variable explorer for Jupyter is shown.