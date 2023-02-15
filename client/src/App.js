import { GlobalStyles } from "./app/components/global";
import Icons from "./app/components/icons";
import Window from "./app/components/window";

function App() {
  return (
    <div>
      <GlobalStyles />
      <Window width={640} height={480} icon={<Icons.DefaultApp/>} title="Sample Window" status="121212121212121212121212121212Sample status string Sample status string Sample status string" navigation="navigation">
            content
      </Window>

    </div>
  );
}

export default App;
