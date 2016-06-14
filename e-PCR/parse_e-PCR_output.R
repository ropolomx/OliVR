library(dplyr)
library(stringr)

panPesti <- read.table("pan-pesti.pcr")

panPesti$primer_type <- character(nrow(panPesti))
panPesti$primer_type[grep("F", panPesti$sts)] <- "Forward"
panPesti$primer_type[grep("R", panPesti$sts)] <- "Reverse"

forward <- panPesti[panPesti$primer_type == "Forward",]
reverse <- panPesti[panPesti$primer_type == "Reverse",]

forward_target <- data.frame(do.call('rbind', strsplit(as.character(forward$seq), '|', fixed=TRUE)))

forward_by_target <- forward_target %>%
                        group_by(X2, X1)

forward_hits <- summarise(forward_by_target, count = n())


forward_hits_summary <- as.data.frame(table(forward_hits$X2))

forward_hits_summary$Num_Seqs <- c(29, 1300, 116, 553, 2)
forward_hits_summary <- forward_hits_summary %>% mutate(perc=((Freq/Num_Seqs)*100))

primer_summary <- merge(forward_hits_summary, reverse_hits_summary, by = "Var1")

atypicalseqnames$V5 <- str_replace(atypicalseqnames$V5, '(^_|_$)','')
str_replace(atypicalseqnames$V5, '_','')

names <- strsplit(as.character(atypicalseqnames2$V5), '(strain|isolate)')
atypicalseqnames2$species <- lapply(names, function(x) as.character(x[1]))
atypicalseqnames2$Strain <- lapply(names, function(x) as.character(x[2]))
