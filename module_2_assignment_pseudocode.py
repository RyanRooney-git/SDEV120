// This pseudocode is intented to
// ask the user about their refrigerator model name,
// height, width, and depth in inches and then print


start
    input modelName = "Please enter the refrigerator model name:"
    input modelIntHeight = "Please enter the refrigerator model interior height in inches:"
    input modelWidth = "Please enter the refrigerator model width in inches:"
    input modelDepth = "Please enter the refrigerator model depth in inches:"
    // calculate refrigeratorCapacity
    refrigeratorCapacity = (modelIntHeight * modelWidth * modelDepth) / 1728
    output print "The refrigerator model name is:" + modelName "and the capacity is" + refrigeratorCapacity
    
end
