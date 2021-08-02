# https://github.com/jkgiesler/healy-viz

require(tidyverse)
require(jsonlite)
require(testthat)

# TODO: 変な属性がついている
# ts -> numeric
# labelled -> as.vector

drop_attr <- function(x){
  attr(x, "label") <- NULL
  attr(x, "format.stata") <- NULL
  attr(x, "labels") <- NULL
  return(x)
}

convert_safer <- function(d){
  as_tibble(d) %>%
    mutate(
      across(where(is.ts), as.numeric),
      across(where(~(class(.) == "labelled")[1]), as.vector),  # ???
      across(everything(), drop_attr)
      )
}
list_col_types <- list(character = "c", integer = "i", numeric = "n", logical = "l", factor = "f", Date = "D", POSIXct = "T")

schema <- list()

(files <- list.files("socviz/data", pattern = "*.rda", full.names = T))
new_datadir = "pysocviz/data"

for (f in files){
  print(basename(f))
  load(f)
  obj_name <- tools::file_path_sans_ext(basename(f))
  d_origin <- convert_safer(get(obj_name))
  schema[[obj_name]] <- lapply(d_origin, function(x) list(class = ifelse("ordered" %in% class(x), "factor", class(x) )))
  for(c in colnames(get(obj_name))){
    if(is.factor(pull(d_origin, c))){
      print(paste("  categorical:", c))
      schema[[obj_name]][[c]] <- append(
        schema[[obj_name]][[c]],
        list(levels = levels(pull(d_origin, c)), ordered = "ordered" %in% class(pull(d_origin, c)))
        )
    }
    expect_equal(length(schema[[obj_name]][[c]][['class']]), 1, label = paste("class name soundness:", c, "in", obj_name))
  }
  write_csv(d_origin, file.path(new_datadir, paste0(obj_name, ".csv")))
  rm(list = obj_name)
}
write_json(schema, path = file.path(new_datadir, "schema.json"), auto_unbox = T)
rm(f, obj_name, schema, d_origin, c)

schema <- read_json(file.path(new_datadir, "schema.json"), simplifyVector = T)

for (f in files){
  load(f)
  obj_name <- tools::file_path_sans_ext(basename(f))
  d_origin <- convert_safer(get(obj_name))
  d <- read_csv(
    file.path(new_datadir, paste0(obj_name, ".csv")),
    col_types = paste0(unlist(lapply(schema[[obj_name]], function(x) list_col_types[x[["class"]] ])), collapse = "")
    )
  for(c in colnames(d)){
    if(is.factor(pull(d, c))){
      d <- mutate(d, !!c := factor(
          pull(d, c),
          levels = schema[[obj_name]][[c]][["levels"]],
          ordered = schema[[obj_name]][[c]][["ordered"]]
          )
        )
    }
  }
  expect_equal(colnames(d), colnames(d_origin), label = paste("column-validation:", obj_name))
  for(c in colnames(d)){
    expect_equal(pull(d, c), pull(d_origin, c), label = paste("value-validation:", c, "in", obj_name))
  }
  rm(list = obj_name)
}
