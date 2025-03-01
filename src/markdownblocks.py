def markdown_to_blocks(markdown):
    '''
    Takes a Markdown srring (representing a full document), splits the string into blocks and returns a llist of block strings
    '''
    output_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if len(block) > 0:
            new_block = ""
            lines = block.split('\n')
            new_lines = []
            for line in lines:
                line = line.strip()
                new_lines.append(line)
            new_block += "\n".join(new_lines)
            output_blocks.append(new_block)
    
    return output_blocks
