import styled from "styled-components";

export const WindowContainer = styled.div`
    position: absolute;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.3);

    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;

`

export const WindowContentContainer = styled.main`
    padding: 10px 30px;
`