import { WindowButton } from "../window-button";
import { WindowTitle } from "../window-title";
import { WindowHeaderButtonsContainer, WindowHeaderIconAndTitleContainer } from "./container";
import { WindowHeaderStyled } from "./styled";

const WindowHeader = ({icon, title}) => {
    return (<WindowHeaderStyled>
        <WindowHeaderIconAndTitleContainer>
            {icon}
            <WindowTitle>{title}</WindowTitle>
        </WindowHeaderIconAndTitleContainer>
        <WindowHeaderButtonsContainer>
            <WindowButton color="#44F8D7"/>
            <WindowButton color="#F84444"/>
        </WindowHeaderButtonsContainer>
    </WindowHeaderStyled>)
}

export default WindowHeader;