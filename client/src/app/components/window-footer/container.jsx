import styled from "styled-components";

export const WindowsFooterStatusBarContainer = styled.p`
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    padding-left: 40px;
    margin-right: 40px;
    box-sizing: border-box;

    display: flex;
    flex-flow: row nowrap;
    align-items: center;

    font-family: 'Poppins';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 21px;

    color: rgba(255, 255, 255, 0.5);
`

export const WindowsFooterNavigationContainer = styled.div`
    padding-right: 40px;
    padding-left: 40px;
    box-sizing: border-box;
    background: rgba(255, 255, 255, 0.05);
    
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;

    border-bottom-right-radius: 5px;
    
    height: 100%;

`