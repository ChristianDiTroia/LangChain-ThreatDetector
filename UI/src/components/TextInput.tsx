export default function TextInput({
  className,
  label,
  value,
  onChange,
}: {
  className?: string;
  label: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
}) {
  return (
    <div className={className}>
      <div className="mb-2">
        <label className="font-bold">{label}</label>
      </div>
      <div className="border-2 rounded-md p-2 min-h-fit bg-gray-900 shadow-xl/50">
        <textarea
          className="outline-none h-fit w-full"
          rows={10}
          value={value}
          onChange={onChange}
        ></textarea>
      </div>
    </div>
  );
}
