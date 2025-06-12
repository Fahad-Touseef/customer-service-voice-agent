import { ResponseFunctionWebSearch } from "openai/resources/responses/responses.mjs";
import React from "react";

import WebSearchIcon from "@/components/icons/WebSearchIcon";

type WebSearchMessageProps = {
  message: ResponseFunctionWebSearch;
};

export function WebSearchMessage({ message }: WebSearchMessageProps) {
  return (
    <div className="flex flex-col w-[70%] relative mb-[-8px]">
      <div>
        <div className="flex flex-col text-sm rounded-[16px]">
          <div className="font-semibold p-3 pl-0 text-gray-700 rounded-b-none flex gap-2">
            <div className="flex gap-2 items-center text-blue-500 ml-[-8px]">
              <WebSearchIcon width={16} height={16} />
              <div className="text-sm font-medium">
                {message.status === "completed"
                  ? "Web search completed"
                  : `Searching the web...`}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
