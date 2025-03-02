def markdown_to_blocks(markdown):
    '''
    Takes a Markdown string (representing a full document), splits the string into blocks and returns a list of block strings
    '''
    output_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if len(block) > 0:
            lines = block.split('\n')
            
            # Check if this is a code block
            if len(lines) >= 2 and lines[0] == "```" and lines[-1] == "```":
                # For code blocks, preserve relative indentation but trim common leading whitespace
                code_lines = lines[1:-1]  # Skip the ``` markers
                
                # Find minimum indentation (if all lines are indented)
                min_indent = float('inf')
                for line in code_lines:
                    if line.strip():  # Skip empty lines
                        indent = len(line) - len(line.lstrip())
                        min_indent = min(min_indent, indent)
                
                if min_indent == float('inf'):
                    min_indent = 0
                
                # Remove that minimum indentation from each line
                processed_code_lines = []
                for line in code_lines:
                    if line.strip():  # If it's not an empty line
                        processed_code_lines.append(line[min_indent:])
                    else:
                        processed_code_lines.append(line)
                
                # Reassemble the code block
                output_blocks.append("```\n" + "\n".join(processed_code_lines) + "\n```")
            else:
                # For non-code blocks, strip each line
                new_lines = []
                for line in lines:
                    new_lines.append(line.strip())
                output_blocks.append("\n".join(new_lines))
    
    return output_blocks