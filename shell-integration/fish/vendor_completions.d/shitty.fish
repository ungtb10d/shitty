function __ksi_completions
    set --local ct (commandline --current-token)
    set --local tokens (commandline --tokenize --cut-at-cursor --current-process)
    printf "%s\n" $tokens $ct | command shitty +complete fish2
end

complete -f -c shitty -a "(__ksi_completions)"
