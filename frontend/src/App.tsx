import "./App.css";
import RecipeMain from "./views/RecipeMain";
import "@netlight-design-system/nds-react/dist/assets/style.css";
import { QueryClient, QueryClientProvider } from "react-query";

function App() {
  const queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryClient}>
      <div className="flex items-center justify-center w-screen p-6 overflow-auto base-background">
        <RecipeMain />
      </div>
    </QueryClientProvider>
  );
}

export default App;
