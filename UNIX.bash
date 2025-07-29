📁 Unix Commands
├── 📂 Navigating the File System
│   ├── 📄 pwd                # Check current directory
│   ├── 📄 ls                 # List files
│   ├── 📄 ls -l              # Long listing
│   ├── 📄 ls -a              # Show hidden files
│   ├── 📄 cd <directory>     # Change directory
│   ├── 📄 cd ..              # Go up one level
│   └── 📄 cd ~               # Go to home directory
│
├── 📂 Managing Files and Directories
│   ├── 📄 touch <file>       # Create file
│   ├── 📄 mkdir <dir>        # Create directory
│   ├── 📄 cp <src> <dest>    # Copy file
│   ├── 📄 mv <src> <dest>    # Move/rename
│   ├── 📄 rm <file>          # Delete file
│   └── 📄 rm -r <dir>        # Delete directory
│
├── 📂 Viewing and Editing Files
│   ├── 📄 cat <file>         # View file
│   ├── 📄 less <file>        # Scrollable view
│   ├── 📄 more <file>        # Page-by-page view
│   ├── 📄 nano <file>        # Edit in nano
│   ├── 📄 vim <file>         # Edit in vim
│   ├── 📄 head <file>        # First lines
│   └── 📄 tail <file>        # Last lines
│
├── 📂 Searching and Finding
│   ├── 📄 grep <pattern> <file>     # Search text
│   ├── 📄 grep -r <pattern> <dir>   # Recursive search
│   ├── 📄 find <dir> -name <file>   # Find by name
│   └── 📄 locate <file>             # Locate files
│
├── 📂 Managing Permissions
│   ├── 📄 ls -l                     # Check permissions
│   ├── 📄 chmod <perm> <file>      # Change permissions
│   └── 📄 chown <user> <file>      # Change ownership
│
├── 📂 Monitoring System Resources
│   ├── 📄 df -h               # Disk usage
│   ├── 📄 du -sh <dir/file>   # Directory/file size
│   ├── 📄 top                 # Live process monitor
│   ├── 📄 htop                # Enhanced monitor
│   └── 📄 ps aux              # Process list
│
├── 📂 Working with Text and Data
│   ├── 📄 sort <file>         # Sort lines
│   ├── 📄 uniq <file>         # Remove duplicates
│   ├── 📄 wc <file>           # Count lines/words
│   └── 📄 sed 's/x/y/g' <file> # Replace text
│
├── 📂 Pipes and Redirection
│   ├── 📄 cmd1 | cmd2         # Pipe output
│   ├── 📄 cmd > file          # Redirect overwrite
│   └── 📄 cmd >> file         # Redirect append
│
├── 📂 Networking Tasks
│   ├── 📄 ping <host>         # Check connectivity
│   ├── 📄 wget <url>          # Download file
│   ├── 📄 curl -O <url>       # Download with curl
│   ├── 📄 ssh user@host       # SSH connection
│   ├── 📄 netstat -tuln       # Show ports (old)
│   └── 📄 ss -tuln            # Show ports (modern)
│
├── 📂 Archiving and Compression
│   ├── 📄 tar -cvf file.tar <files>   # Create archive
│   ├── 📄 tar -xvf file.tar           # Extract archive
│   ├── 📄 gzip <file>                 # Compress
│   └── 📄 gunzip <file.gz>            # Decompress
│
├── 📂 Background Tasks
│   ├── 📄 cmd &               # Run in background
│   ├── 📄 jobs                # List background jobs
│   └── 📄 kill <PID>          # Kill process
│
└── 📂 Getting Help
    ├── 📄 man <command>       # Manual page
    └── 📄 <command> --help    # Quick help
