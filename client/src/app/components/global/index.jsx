import { createGlobalStyle } from "styled-components";
import Background from "./background.png";
import Poppins300 from "./Poppins-Light.ttf";
import Poppins400 from "./Poppins-Regular.ttf";
import Poppins500 from "./Poppins-Medium.ttf";
import Poppins700 from "./Poppins-Bold.ttf";

export const GlobalStyles = createGlobalStyle`
    
    * {
        margin: 0;
        padding: 0;
        user-select: none;
    }

    html, body {
        width: 100vw;
        height: 100vh;
    }

    @font-face {
        font-family: "Poppins";
        font-style: normal;
        font-weight: 300;
        src: url(${Poppins300});
    }

    @font-face {
        font-family: "Poppins";
        font-style: normal;
        font-weight: 400;
        src: url(${Poppins400});
    }

    @font-face {
        font-family: "Poppins";
        font-style: normal;
        font-weight: 500;
        src: url(${Poppins500});
    }

    @font-face {
        font-family: "Poppins";
        font-style: normal;
        font-weight: 700;
        src: url(${Poppins700});
    }

    body {
        background: url(${Background}) no-repeat center/cover;
        font-family: "Poppins", serif;
        font-weight: 400;
    }

`
