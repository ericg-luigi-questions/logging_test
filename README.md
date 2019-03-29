

```
$ printenv
...
LUIGI_CONFIG_PARSER=toml
LUIGI_CONFIG_PATH=./luigi.toml
...

```

Run with: 

```
luigi --module logging_test.mytask LoggingTask --local-scheduler
```