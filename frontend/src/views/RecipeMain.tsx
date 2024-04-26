import robot from "../assets/chefPrimary.svg";
import egg from "../assets/fried-egg-svgrepo-com.svg";
import { TextField, Button } from "@netlight-design-system/nds-react";
import HealthStatus from "../components/HealthStatus";
import { recipe } from "../services/RecipeService";
import { useMutation } from "react-query";
import { useEffect, useState } from "react";
import { Recipe } from "../types/types";
import Output from "./Output";

function RecipeMain() {
  const { mutate, isLoading, data, isError } = useMutation(recipe);
  const [url, setUrl] = useState<string>("");
  const [recipeData, setRecipe] = useState<Recipe>();

  useEffect(() => {
    setRecipe(data);
  }, [data]);

  function handleClick() {
    if (url) {
      mutate(url);
    }
  }
  const onBack = () => {
    setRecipe(undefined);
  };
  if (isLoading) {
    return (
      <>
        <div className="flex flex-col justify-center items-center bg-white max-w-[50vw] rounded-md  p-4 gap-4">
          <img src={egg} className="w-16 h-auto " />
        </div>
      </>
    );
  }

  if (recipeData) {
    return (
      <>
        <div className="flex flex-col justify-center items-center bg-white max-w-[50vw]   rounded-md  p-4 gap-4">
          <Output data={recipeData} onBack={onBack}></Output>
        </div>
      </>
    );
  }
  return (
    <div className="flex flex-col justify-center items-center bg-white max-w-[50vw] rounded-md  p-4 gap-4">
      <img src={robot} className="w-32 h-auto" />
      <h1 className="text-4xl font-bold text-primary">Chatatouille</h1>
      <TextField
        inputId="url"
        label="URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      ></TextField>
      <Button onClick={handleClick}>Get recipe</Button>
      <HealthStatus></HealthStatus>
      {isError ? (
        <p className="text-primary">
          Failed to create recipe, please check logs 🫣
        </p>
      ) : (
        ""
      )}
    </div>
  );
}

export default RecipeMain;
