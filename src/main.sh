usage()
{
    echo "--scan <IP>"
    echo "--dir -w <wordlists> <IP>"
}

case "$1" in
    --scan)
        case "$#" in
            2)
                python3 scanner/scanner.py $2
            ;;
            *)
                usage
            ;;
        esac
    ;;
    *)
        usage
    ;;
esac
