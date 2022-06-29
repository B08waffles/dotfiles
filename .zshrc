# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi

# First path is for the cslint plugin
export PATH=/home/brandon/.dotnet/tools:$PATH
# Env for the tex to html thing
export kodymirus_root=/home/brandon/Documents/yummo/Seeitworks
export PATH="$HOME/.emacs.d/bin:$PATH"
alias shadow='zsh ~/Documents/bash/Add_Shadows.sh'
alias config='/usr/bin/git --git-dir=$HOME/dotgit/ --work-tree=$HOME'
neofetch
