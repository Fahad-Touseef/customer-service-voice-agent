import React from "react";

import ShuffleIcon from "@/components/icons/ShuffleIcon";
import { ToolCall } from "@/lib/types";

type HandoffMessageProps = {
  message: ToolCall;
};

export function HandoffMessage({ message }: HandoffMessageProps) {
  let agentName: string;
  if (message?.output) {
    agentName = message?.output?.match(/'assistant':\s*'([^']+)'/)?.[1] || "";
  } else {
    agentName = message.name;
  }

  return (
    <div className="flex flex-col w-[70%] relative mb-[-8px]">
      <div>
        <div className="flex flex-col text-sm rounded-[16px]">
          <div className="font-semibold p-3 pl-0 text-gray-700 rounded-b-none flex gap-2">
            <div className="flex gap-2 items-center text-blue-500 ml-[-8px]">
              <ShuffleIcon width={16} height={16} />
              <div className="text-sm font-medium">
                {message.status === "completed"
                  ? `Transferred to ${agentName}`
                  : `Transferring conversation...`}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
