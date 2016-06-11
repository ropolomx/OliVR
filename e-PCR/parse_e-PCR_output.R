library(dplyr)

panPesti <- read.delim("~/virology/Pestivirus/e-PCR/pan-pesti.pcr")
panPesti$primer_type <- character(nrow(panPesti))
panPesti$primer_type[grep("F", panPesti$sts)] <- "Forward"
panPesti$primer_type[grep("R", panPesti$sts)] <- "Reverse"

forward <- panPesti[panPesti$primer_type == "Forward",]
reverse <- panPesti[panPesti$primer_type == "Reverse",]

forward2 <- within(forward, 
                   target <- data.frame(do.call('rbind',
                                                strsplit(as.character(forward$seq),
                                                         '|', fixed=TRUE))))
forward_hits <- table(forward2$target[2][unique(forward2$seq),])

reverse2 <- within(reverse,
                   target <- data.frame(do.call('rbind',
                                                strsplit(as.character(reverse$seq),
                                                         '|', fixed=TRUE))))
reverse_hits <- table(reverse2$target[2][unique(reverse2$seq),])