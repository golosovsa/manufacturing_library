import { WindowsFooterNavigationContainer, WindowsFooterStatusBarContainer } from "./container";
import { WindowFooterStyled } from "./styled";

const WindowFooter = ({status, navigation}) => {
    return (
        <WindowFooterStyled title={status}>
            <WindowsFooterStatusBarContainer children={status} />
            <WindowsFooterNavigationContainer children={navigation}/>
        </WindowFooterStyled>
    );
}

export default WindowFooter;