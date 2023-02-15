import WindowFooter from "../window-footer";
import WindowHeader from "../window-header";
import { WindowContainer, WindowContentContainer } from "./container";
import { StyledWindow } from "./styled";

const Window = ({width, height, icon, title, children, status, navigation}) => {
    return (
        <WindowContainer>
            <StyledWindow style={{width: `${width}px`, height: `${height}px`}}>
                <WindowHeader icon={icon} title={title} />
                <WindowContentContainer children={children}/>
                <WindowFooter status={status} navigation={navigation}/>
            </StyledWindow>
        </WindowContainer>
    );
}

export default Window;