import "./App.css";
import RecipeMain from "./views/RecipeMain";
import "@netlight-design-system/nds-react/dist/assets/style.css";
import { QueryClient, QueryClientProvider } from "react-query";

function App() {
  const queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryClient}>
      <div className="flex flex-col items-center justify-center w-screen h-screen p-6">
        <RecipeMain />
      </div>
    </QueryClientProvider>
  );
}

export default App;
