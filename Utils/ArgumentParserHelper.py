import argparse

def GetArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--log", help="Logging level (DEBUG, INFO, ERROR)")
    parser.add_argument("-o", "--output", help="Name of file outlog for logs. If empty, default is console output.")
    args = parser.parse_args()
    level = Level[args.log] or Level.DEBUG
    output = args.output or "CONSOLE"

    return output, level