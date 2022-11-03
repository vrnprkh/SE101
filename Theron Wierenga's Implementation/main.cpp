//Color an x,y square with a specific color
void colorSquare(byte x, byte y, uint32_t color, bool on)
{
    if( (x >= 0) && (x < 4) && (y >= 0) && (y < 8)) //is it a legal square on the board
    {
        int num1 = (y << 5) + (x << 1); //y * 32 + x * 2
        int num2 = num1 + 1;
        int num3 = (y << 5) + 31 - (x << 1); // y * 32 + 31 - x * 2
        int num4 = num3 - 1; //Adds a short delay
        pixels.setPixelColor(num1, color);
        delay(1);
        pixels.setPixelColor(num2, color);
        delay(1);
        pixels.setPixelColor(num3, color);
        delay(1);
        pixels.setPixelColor(num4, color);
        delay(1);
        if(on)
            pixels.show();
    }
}

//Color a chessboard with blue and red squares
void standBoard()
{
    for (int y = 0; y < 4; ++y)
    {
        for (int x{0}; x < 4; ++x)
        {
            colorSquare(x * 2, y * 2, colors[RED], false);
            colorSquare(x * 2 + 1, y * 2, colors[BLUE], false);
            colorSquare(x * 2, y * 2 + 1, colors[BLUE], false);
            colorSquare(x * 2 + 1, y * 2 + 1, colors[RED], false);
        }
    }
    pixels.show();
}

//Color all squares, red for error alert, blue for checkmate
void colorBoard(uint32_t color)
{
    for (int i{0}; i < NUMPIXELS; ++i)
    {
        pixels.setPixelColor(i, color);
    }
    pixels.show();
}

